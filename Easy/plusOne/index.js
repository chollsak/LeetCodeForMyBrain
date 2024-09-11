/**
 * @param {number[]} digits
 * @return {number[]}
 */
let resultArr;
let resultNum;

var plusOne = function(digits) {
    //long arr
    if(digits.length >= 10){
        for (let i = digits.length - 1; i >= 0; i--) {
            if(digits[i] < 9){
                digits[i] ++
                return digits
            }else{
                digits[i] = 0;
            }
        }
        return resultArr = [1, ...digits];

    //short arr
    }else{
        let number = parseInt(digits.join(''), 10);
        resultNum = number + 1
        resultArr = String(resultNum).split("").map((resultNum) => {
            return Number(resultNum)
        })
    }

    return resultArr

};

let inputArr = [6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3];

console.log(plusOne((inputArr)))

//----------------------------------------------------------------

//f!! i just know that there is BigInt()!

// /**
//  * @param {number[]} digits
//  * @return {number[]}
//  */
// var plusOne = function(digits) {
//     digits = digits.join('');
//     digits = BigInt(digits) + BigInt(1);
//     return digits.toString().split('');
// };
