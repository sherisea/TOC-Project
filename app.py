import os
from bottle import route, run, request, abort, static_file
from fsm import TocMachine

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']
machine = TocMachine(
    states=[
        'user',
        'azurlane',
        'whiteeagle',
            'eagle',
	    'esex',
        'royal',
            'opai',
        'sakura',
            'loli',
        'ironblood',
            'hinnyuu',
	'eastempire',
	    'sister',
	'freedom',
	    'triumph',
	'holysee',
	    'thigh',
	'northunion',
	    'abpopa',
	
    ],
    transitions=[
        {
            'trigger': 'wakeup',
            'source': 'user',
            'dest': 'azurlane',
        },
        {
            'trigger': 'advance',
            'source': [
                'user',
                'azurlane',
                'whiteeagle',
                    'eagle',
	            'esex',
                'royal',
                    'opai',
                'sakura',
                    'loli',
                'ironblood',
                    'hinnyuu',
		'eastempire',
		    'sister',
		'freedom',
		    'triumph',
		'holysee',
		    'thigh',
		'northunion',
		    'abpopa',
            ],
            'dest': 'azurlane',
            'conditions': 'is_going_to_azurlane'
        },
        {
            'trigger': 'advance',
            'source': 'azurlane',
            'dest': 'whiteeagle',
            'conditions': 'is_going_to_whiteeagle'
        },
            {
            'trigger': 'advance',
            'source': 'whiteeagle',
            'dest': 'eagle',
            'conditions': 'is_going_to_eagle'
            },
	    {
            'trigger': 'advance',
            'source': 'whiteeagle',
            'dest': 'esex',
            'conditions': 'is_going_to_esex'
            },

        {
            'trigger': 'advance',
            'source': 'azurlane',
            'dest': 'royal',
            'conditions': 'is_going_to_royal'
        },
            {
            'trigger': 'advance',
            'source': 'royal',
            'dest': 'opai',
            'conditions': 'is_going_to_opai'
            },

        {
            'trigger': 'advance',
            'source': 'azurlane',
            'dest': 'sakura',
            'conditions': 'is_going_to_sakura'
        },
            {
            'trigger': 'advance',
            'source': 'sakura',
            'dest': 'loli',
            'conditions': 'is_going_to_loli'
            },

        {
            'trigger': 'advance',
            'source': 'azurlane',
            'dest': 'ironblood',
            'conditions': 'is_going_to_ironblood'
        },
            {
            'trigger': 'advance',
            'source': 'ironblood',
            'dest': 'hinnyuu',
            'conditions': 'is_going_to_hinnyuu'
            },

        {
            'trigger': 'advance',
            'source': 'azurlane',
            'dest': 'eastempire',
            'conditions': 'is_going_to_eastempire'
        },
            {
            'trigger': 'advance',
            'source': 'eastempire',
            'dest': 'sister',
            'conditions': 'is_going_to_sister'
            },
        {
            'trigger': 'advance',
            'source': 'azurlane',
            'dest': 'freedom',
            'conditions': 'is_going_to_freedom'
        },
            {
            'trigger': 'advance',
            'source': 'freedom',
            'dest': 'triumph',
            'conditions': 'is_going_to_triumph'
            },
        {
            'trigger': 'advance',
            'source': 'azurlane',
            'dest': 'holysee',
            'conditions': 'is_going_to_holysee'
        },
            {
            'trigger': 'advance',
            'source': 'holysee',
            'dest': 'thigh',
            'conditions': 'is_going_to_thigh'
            },
        {
            'trigger': 'advance',
            'source': 'azurlane',
            'dest': 'northunion',
            'conditions': 'is_going_to_northunion'
        },
            {
            'trigger': 'advance',
            'source': 'northunion',
            'dest': 'abpopa',
            'conditions': 'is_going_to_abpopa'
            },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)




@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if machine.state == 'user':
           machine.wakeup(event)
        else:
           machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloder=True)
