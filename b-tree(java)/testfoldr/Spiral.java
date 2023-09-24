package testfoldr;

class Spiral {
    static int[][] spiral(int rows, int colums) {
        int[][] res = new int[rows][colums];
        int i = 1;
        int leftborder = 0;
        int rightborder = colums - 1;
        int topborder = 0;
        int botborder = rows - 1;
        while (i <= rows * colums) {
            for (int j = leftborder; j <= rightborder; j++) {
                res[topborder][j] = i++;
            }
            topborder++;
            if(i > rows*colums){
                break;
            }
            for (int j = topborder; j <= botborder; j++) {
                res[j][rightborder] = i++;
            }
            rightborder--;
            if(i > rows*colums){
                break;
            }
            for (int j = rightborder; j >= leftborder; j--) {
                
                res[botborder][j] = i++;
            }
            botborder--;
            if(i > rows*colums){
                break;
            }
            for (int j = botborder; j >= topborder; j--) {
                res[j][leftborder] = i++;
            }
            leftborder++;
        }
        return res;
    }

    static String printspiral(int[][] spi){
        for (int i = 0; i < spi.length; i++) {
            for (int j = 0; j < spi[i].length; j++) {
                System.out.print(String.format("%4s", spi[i][j]));
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {

        int[][] a = Spiral.spiral(1, 1);



    }
}

