import json
import asyncio

message = False

@asyncio.iscoroutine
async def listen(scope, receive, send):
    while True:
        global message

        event = await receive()

        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept'
            })

        if event['type'] == 'websocket.disconnect':
            break

        if event['type'] == 'websocket.receive':
            if event['text'] == 'listener':
                while True:
                    if message:
                        await send({
                            'type': 'websocket.send',
                            "text": 'BRAODCATS'
                        })
                        message = False


# @asyncio.iscoroutine
async def listen_ap(scope,receive, send):

    while True:
        global message

        event= await receive()

        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept'
            })

        if event['type'] == 'websocket.disconnect':
            break

        if event['type'] == 'websocket.receive':
            if event['text'] == 'appointment':
                message = True
                await send({
                    'type': 'websocket.send',
                    "text": json.dumps(event)
                })

async def main(scope, receive, send):
    t1 = asyncio.create_task(listen_ap(scope, receive, send))
    t2 = asyncio.create_task(listen(scope, receive, send))
    await t1
    await t2

async def websocket_application(scope, receive, send):
    asyncio.run(main(scope, receive, send))
    # while True:
    #     global message
    #
    #     event= await receive()
    #
    #     if event['type'] == 'websocket.connect':
    #         await send({
    #             'type': 'websocket.accept'
    #         })
    #
    #     if event['type'] == 'websocket.disconnect':
    #         break
    #
    #     if event['type'] == 'websocket.receive':
    #         if event['text'] == 'appointment':
    #             message = True
    #             await send({
    #                 'type': 'websocket.send',
    #                 "text": json.dumps(event)
    #             })
    #

