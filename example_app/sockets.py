async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text('Hello, World!')
    await websocket.close()
