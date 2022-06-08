# coding: utf-8

"""
    Knowledge-Graph Query API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsearch.cps.apis.kg.query.api_client import ApiClient
from deepsearch.cps.apis.kg.query.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class NodeSearchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_nodes_approximately(self, epsilon, names, **kwargs):  # noqa: E501
        """search_nodes_approximately  # noqa: E501

        Search for nodes that have an approximate name.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_nodes_approximately(epsilon, names, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float epsilon: similarity (required)
        :param list[str] names: names contained in node (required)
        :param int limit: Maximum number of returned nodes, use -1 for all.
        :param str category: Search only for nodes in this category. By default, we search in all categories.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NodesResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.search_nodes_approximately_with_http_info(epsilon, names, **kwargs)  # noqa: E501

    def search_nodes_approximately_with_http_info(self, epsilon, names, **kwargs):  # noqa: E501
        """search_nodes_approximately  # noqa: E501

        Search for nodes that have an approximate name.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_nodes_approximately_with_http_info(epsilon, names, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float epsilon: similarity (required)
        :param list[str] names: names contained in node (required)
        :param int limit: Maximum number of returned nodes, use -1 for all.
        :param str category: Search only for nodes in this category. By default, we search in all categories.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NodesResponseModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'epsilon',
            'names',
            'limit',
            'category'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_nodes_approximately" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'epsilon' is set
        if self.api_client.client_side_validation and ('epsilon' not in local_var_params or  # noqa: E501
                                                        local_var_params['epsilon'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `epsilon` when calling `search_nodes_approximately`")  # noqa: E501
        # verify the required parameter 'names' is set
        if self.api_client.client_side_validation and ('names' not in local_var_params or  # noqa: E501
                                                        local_var_params['names'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `names` when calling `search_nodes_approximately`")  # noqa: E501

        if self.api_client.client_side_validation and 'epsilon' in local_var_params and local_var_params['epsilon'] > 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `epsilon` when calling `search_nodes_approximately`, must be a value less than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'epsilon' in local_var_params and local_var_params['epsilon'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `epsilon` when calling `search_nodes_approximately`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'epsilon' in local_var_params and local_var_params['epsilon'] is not None:  # noqa: E501
            query_params.append(('epsilon', local_var_params['epsilon']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'category' in local_var_params and local_var_params['category'] is not None:  # noqa: E501
            query_params.append(('category', local_var_params['category']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'names' in local_var_params:
            body_params = local_var_params['names']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/searchNodes/approximately', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodesResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_nodes_regex(self, regular_expressions, **kwargs):  # noqa: E501
        """search_nodes_regex  # noqa: E501

        Search for nodes that have a name that matches the regular expressions.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_nodes_regex(regular_expressions, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] regular_expressions: regular expressions for node-names (required)
        :param int limit: Maximum number of returned nodes, use -1 for all.
        :param str category: Search only for nodes in this category. By default, we search in all categories.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NodesResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.search_nodes_regex_with_http_info(regular_expressions, **kwargs)  # noqa: E501

    def search_nodes_regex_with_http_info(self, regular_expressions, **kwargs):  # noqa: E501
        """search_nodes_regex  # noqa: E501

        Search for nodes that have a name that matches the regular expressions.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_nodes_regex_with_http_info(regular_expressions, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] regular_expressions: regular expressions for node-names (required)
        :param int limit: Maximum number of returned nodes, use -1 for all.
        :param str category: Search only for nodes in this category. By default, we search in all categories.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NodesResponseModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'regular_expressions',
            'limit',
            'category'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_nodes_regex" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'regular_expressions' is set
        if self.api_client.client_side_validation and ('regular_expressions' not in local_var_params or  # noqa: E501
                                                        local_var_params['regular_expressions'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `regular_expressions` when calling `search_nodes_regex`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'category' in local_var_params and local_var_params['category'] is not None:  # noqa: E501
            query_params.append(('category', local_var_params['category']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'regular_expressions' in local_var_params:
            body_params = local_var_params['regular_expressions']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/searchNodes/regex', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodesResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
