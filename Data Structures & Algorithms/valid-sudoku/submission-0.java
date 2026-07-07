class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> set = new HashSet<>();
        int row = 0;
        int column = 0;
        int startRow;
        int startColumn;
        int r;
        int c;
        while (row < 9) {
            for (int i = 0; i < board.length; i++) {
                if (board[row][i] == '.') {
                    continue;
                }
                if (!set.add(board[row][i])) {
                    return false;
                }
            }
            set.clear();
            row++;
        }
        
        while (column < 9){
            for (int i = 0; i < board.length; i++) {
                if (board[i][column] == '.') {
                    continue;
                }
                if (!set.add(board[i][column])) {
                    return false;
                }
            }
            set.clear();
            column++;
        }

        for (int b = 0; b < board.length; b++) {
            startRow = (b / 3) * 3;
            startColumn = (b % 3) * 3;
            for (int j = 0; j < board.length; j++) {
                r = startRow + (j/3);
                c = startColumn + (j%3);
                if (board[r][c] == '.') {
                    continue;
                }
                if (!set.add(board[r][c])) {
                    return false;
                }
            }
            set.clear();        
        }

        return true;
    }
}
