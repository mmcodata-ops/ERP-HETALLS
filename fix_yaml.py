with open('render.yaml', 'r') as f:
    content = f.read()
if 'autoDeploy: true' not in content:
    content = content.replace('name: hetalls-erp-b', 'name: hetalls-erp-b\n    autoDeploy: true')
    content = content.replace('name: hetalls-erp\n', 'name: hetalls-erp\n    autoDeploy: true\n')
    with open('render.yaml', 'w') as f:
        f.write(content)
