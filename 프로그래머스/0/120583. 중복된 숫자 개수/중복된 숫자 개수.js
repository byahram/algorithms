const solution = (array, n) => array.reduce((a,b) => n === b ? a+1 : a,0)
