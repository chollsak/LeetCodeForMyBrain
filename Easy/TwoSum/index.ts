function twoSum(nums: number[], target: number): number[] {
    let numArr = nums;
    let tempArr: number[] = []; // 3 2 
    let result: number[] = []; 

    for (let i = 0; i < numArr.length; i++) {
        let val = numArr[i]; // 3 2 4
        let complement = target - val; //// console.log(twoSum([3,2,4], 6)) 3 4 2

        // Check if the complement is already in tempArr
        let foundIndex = tempArr.findIndex(num => num === complement);

        if (foundIndex !== -1) {
            // If found, return the indices
            let firstIndex = tempArr.indexOf(complement); 
            result.push(firstIndex); // 1
            result.push(i); //2
            return result;
        }

        // If complement not found, push the current value and its index to tempArr
        tempArr.push(val);
    }

    return result;
}

// console.log(twoSum([2,7,11,15], 9))
// console.log(twoSum([3,2,4], 6))
// console.log(twoSum([3,3], 6))
console.log(twoSum([3,2,3], 6))