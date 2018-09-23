from app import app
from flask import request, make_response, jsonify
from .models import Orders
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
import base64


log = app.logger

#===========================================================================
#    client side request to http://127.0.0.1:9090/
#===========================================================================
@app.route('/', methods=['POST'])
def message_process():
    req = request.get_json(silent=True, force=True)
    log.info("Request: %s", req)

    try:
        action = req.get('queryResult').get('action')
        log.info("Action: %s", action)
    except AttributeError:
        return make_response(jsonify({'fulfillmentText': "Improper Action defined..."}))

    res = "Unsuccessful parameter parsing."
    if action == 'StatusOrder.StatusOrder-custom':
        res = check_order_status(req)
    else:
        return make_response(jsonify({'fulfillmentText': "Unexpected action defined."}))

    print('Action: ' + action)
    print('Response: ' + res)

    return make_response(jsonify({'fulfillmentText': res}))



def check_order_status(req):
    order_id = req['queryResult']['parameters']['orderNumber']
    print("Your Order ID:" + order_id)
    log.info("Order Id: %s", order_id)
    order = Orders.query.filter_by(order_id=order_id).first()
    log.info("Fetched order: ", order)
    if order is not None:
        return prettify_order(order)
        # return productDetails(order_id)
    else:
        return "Sorry no orders were found for order id: '" + order_id + "'"


def prettify_order(order):
    # return productDetails(order)

    return "You order ({}) place on {} will be delivered by {}" .format(order.order_id, order.order_date, order.delivery_date)


@app.errorhandler(404)

def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)






#===========================================================================
#    client side request to http://127.0.0.1:9090/
#===========================================================================
@app.route('/test', methods=['POST','GET'])
def test():
    url = "http://127.0.0.1:9090/"
    headers = {'Content-Type': 'application/text'}

    data  = '{ ' \
            '"queryResult": {' \
            '            "queryText": "order status", ' \
            '              "action": "StatusOrder.StatusOrder-custom",  ' \
            '               "parameters": { ' \
            '                               "orderNumber": "abc123" ' \
            '                               } ' \
            '               } ' \
            '}'
    response = requests.post(url,headers=headers, data=data)
    return response.content



@app.route('/orders/<id_order>', methods=['POST','GET'])
def productDetails(id_order):
    print(id_order)  #EEMUA5RXT71SLJT25737B4PBF45Z19HD
    url = "http://35.196.130.106/api/orders/"+id_order+"?output_format=JSON"
    print(url)
    response = requests.get(url, auth=HTTPBasicAuth('TKVLNFEMB2CJ8KR1YD3U4T6GFZ1NJMTH', ''))
    print(response)
    if response.status_code in [200]:
        product_name = ''
        output = json.loads(response.content)
        # print(output['order_detail']['product_name'])
        # return "Your Prduct: {} and Price {}".format(output['order']['order_rows']['product_name'], output['order']['total_paid'])
        product_infos = output['order']['associations']['order_rows']
        product_paid_amount = output['order']['total_paid_tax_excl']
        order_by_payment = output['order']['payment']
        for product_info in product_infos:
            product_name =  product_info['product_name']
        print(product_name)
        print(product_paid_amount)
        print(order_by_payment)
        return "Your Product Name:{} and Price:{} and Order by:{}".format(product_name,product_paid_amount,order_by_payment)
    else:
        return "Sorry, no order found "+str(id_order)




