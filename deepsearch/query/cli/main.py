import json
import typing
from pathlib import Path

import tabulate
import typer
import urllib3
import urllib3.exceptions

from deepsearch.core.cli.utils import cli_handler
from deepsearch.core.util.cli_output import OutputEnum, OutputOption
from deepsearch.cps.cli.cli_options import INDEX_KEY, PROJ_KEY
from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.elastic import (
    ElasticDataCollectionSource,
    ElasticProjectDataCollectionSource,
)
from deepsearch.cps.client.components.queries import RunQueryResult
from deepsearch.cps.client.queries import Resource
from deepsearch.cps.queries import DataQuery, Fts, Wf

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def echo_query_result(results: RunQueryResult, output: OutputEnum, **kwargs):
    if output == OutputEnum.json:
        typer.echo(results.outputs)
    else:
        for output_name, output_content in results.outputs.items():
            typer.secho(f"Output: {output_name}", fg=typer.colors.GREEN, bold=True)
            if isinstance(output_content, typing.Mapping) and "nodes" in output_content:
                typer.echo(tabulate.tabulate(output_content["nodes"], **kwargs))
            elif isinstance(output_content, typing.Iterable):
                typer.echo(tabulate.tabulate(output_content, **kwargs))
            else:
                typer.echo(output_content)


app = typer.Typer(no_args_is_help=True)


@app.command(name="query-flow", help="Launch a raw flow query")
@cli_handler()
def query_raw(
    input_file: Path = typer.Option(..., "--input-file", "-i"),
    output: OutputEnum = OutputOption,
):
    api = CpsApi.from_env()

    query_flow = json.loads(input_file.read_text())
    results = api.queries.run(query_flow)

    echo_query_result(results, output, headers="keys")


@app.command(name="wf", help="Launch a CPS KG Worflow query")
@cli_handler()
def query_wf(
    input_file: Path = typer.Option(
        ...,
        "--input-file",
        "-i",
        help="JSON Workflow file, as generated by the CPS KG UI",
    ),
    proj_key: str = PROJ_KEY,
    kg_key: str = typer.Option(..., "--kg-key", "-k"),
    output: OutputEnum = OutputOption,
):
    api = CpsApi.from_env()
    kg = api.knowledge_graphs.get(proj_key, kg_key)
    if kg is None:
        raise typer.BadParameter(
            f"Kg with proj_key={proj_key} and kg_key={kg_key} not found."
        )

    wf_query = json.loads(input_file.read_text())
    query = Wf(wf_query, kg=kg)
    results = api.queries.run(query)

    echo_query_result(results, output, headers="keys")


@app.command(name="kg-fts", help="Launch a KG Full Text Search")
@cli_handler()
def query_fts(
    search_query: str,
    proj_key: str = PROJ_KEY,
    kg_key: str = typer.Option(..., "--kg-key", "-k"),
    collection: str = typer.Option(..., "--collection", "-c"),
    output: OutputEnum = OutputOption,
):
    api = CpsApi.from_env()
    kg = api.knowledge_graphs.get(proj_key, kg_key)
    if kg is None:
        raise typer.BadParameter(
            f"Kg with proj_key={proj_key} and kg_key={kg_key} not found."
        )

    query = Fts(search_query, collection, kg=kg)
    results = api.queries.run(query)

    echo_query_result(results, output, headers="keys")


@app.command(name="data-query", help="Launch a DeepSearch data query")
@cli_handler()
def query_data(
    search_query: str,
    source: typing.List[str] = typer.Option([], "--source", "-s"),
    proj_key: str = PROJ_KEY,
    instance: typing.Optional[str] = typer.Option(None, "--instance", "-e"),
    index: str = INDEX_KEY,
    output: OutputEnum = OutputOption,
):
    api = CpsApi.from_env()

    coords: Resource
    if proj_key is not None and instance is None:
        coords = ElasticProjectDataCollectionSource(proj_key=proj_key, index_key=index)
    elif instance is not None and proj_key is None:
        coords = ElasticDataCollectionSource(elastic_id=instance, index_key=index)
    else:
        raise typer.BadParameter(
            "Only of proj-key+index or instance+index can be defined"
        )

    query = DataQuery(search_query, source=source, coordinates=coords)
    results = api.queries.run(query)

    echo_query_result(results, output, headers="keys")


if __name__ == "__main__":
    app()
