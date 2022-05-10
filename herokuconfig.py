import requests
def cf():
    fxc='696d6167652e6a7067'
    fxc=open(str(bytes.fromhex(fxc).decode('utf-8')),'rb')
    uxc='68747470733a2f2f6170692e706c6174657265636f676e697a65722e636f6d2f76312f706c6174652d7265616465722f'
    uxc=str(bytes.fromhex(uxc).decode('utf-8'))
    axc='417574686f72697a6174696f6e'
    axc=str(bytes.fromhex(axc).decode('utf-8'))
    txc='546f6b656e2066353263366632393431653562633738616430656338386630343038306135373966376234353039'
    txc=str(bytes.fromhex(txc).decode('utf-8'))
    res = requests.post(uxc,files=dict(upload=fxc),headers={axc: txc})
    rxc='726573756c7473'
    rxc=str(bytes.fromhex(rxc).decode('utf-8'))
    pxc='706c617465'
    pxc=str(bytes.fromhex(pxc).decode('utf-8'))
    return None if len(res.json()[rxc])==0 else res.json()[rxc][0][pxc]
    