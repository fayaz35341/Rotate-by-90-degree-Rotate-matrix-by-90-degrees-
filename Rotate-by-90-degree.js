class Solution {
    rotateMatrix(matrix) {
        // code here
        let n=matrix.length

        for (let i=0;i<n;i++){
            for (let j=i+1;j<n;j++){
                [matrix[j][i],matrix[i][j]]=[matrix[i][j],matrix[j][i]]
            }
        };
    
        for (let i=0;i<n;i++) {
            let top=0
            let bot=n-1
            while(top<bot){
                [matrix[top][i],matrix[bot][i]]=[matrix[bot][i],matrix[top][i]]
                top++
                bot--
            }
        };
    }
}
