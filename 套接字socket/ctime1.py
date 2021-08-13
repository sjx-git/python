def application(environ,start_response):
    #因为application只能规定只能返回，response body部分，但是还需要请求头和请求行，所以这个时候就得用到第二个参数了
    status = '404 Not Found'
    response_headers = [
        #需要用元祖
    ]
    start_response(status,response_headers)
    return '404的请求'
