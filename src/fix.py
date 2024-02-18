from interpreter import var_pro
let = {'john': '43'}
result = var_pro("Some text {john} more text", let)
print(result)