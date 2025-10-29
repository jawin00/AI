def alphabeta(node, depth, alpha, beta, maximizingPlayer):
   
    if depth == 0 or 'children' not in node:
        return node['value'], [node['value']]
    
    if maximizingPlayer:
        maxEval = -float('inf')
        path = []
        for child in node['children']:
            eval, child_path = alphabeta(child, depth-1, alpha, beta, False)
            if eval > maxEval:
                maxEval = eval
                path = [node['value']] + child_path
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
        return maxEval, path
    else:
        minEval = float('inf')
        path = []
        for child in node['children']:
            eval, child_path = alphabeta(child, depth-1, alpha, beta, True)
            if eval < minEval:
                minEval = eval
                path = [node['value']] + child_path
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval, path

tree = {
    'value': 'A',
    'children': [
        {'value': 'B', 'children': [
            {'value': 3}, {'value': 12}, {'value': 8}
        ]},
        {'value': 'C', 'children': [
            {'value': 2}, {'value': 4}, {'value': 6}
        ]},
        {'value': 'D', 'children': [
            {'value': 14}, {'value': 5}, {'value': 2}
        ]}
    ]
}

value, path = alphabeta(tree, 3, -float('inf'), float('inf'), True)
print("Root value:", value)
print("Path to root value:", " -> ".join(map(str, path)))
