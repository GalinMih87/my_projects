function calcSum() {
    let num1 = document.getElementById('num1').value;
    let num2 = document.getElementById('num2').value;
    let coefficient1 = document.getElementById('coefficient1').value;
    let coefficient2 = document.getElementById('coefficient2').value;

    let result1 = Number(num1) * Number(coefficient1);
    let result2 = Number(num2) * Number(coefficient2);
    let sum = result1 + result2;

    document.getElementById('result1').value = result1;
    document.getElementById('result2').value = result2;
    document.getElementById('sum').value = sum;
}
