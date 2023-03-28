#!/usr/bin/node
function factorial (n) {
    if (isNaN(parseInt(n))) {
        return (1);
    }
    if (n === 1) {
        return (1);
    }
    return (n * factorial(n - 1));
}
console.log(factorial(parseInt(process.argv[2])));