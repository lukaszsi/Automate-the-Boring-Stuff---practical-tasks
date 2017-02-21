class CharacterPictureGrid {
    public static void main(String[] args) {
        String[][] grid = {
        {".", ".", ".", ".", ".", "."},
        {".", "O", "O", ".", ".", "."},
        {"O", "O", "O", "O", ".", "."},
        {"O", "O", "O", "O", "O", "."},
        {".", "O", "O", "O", "O", "O"},
        {"O", "O", "O", "O", "O", "."},
        {"O", "O", "O", "O", ".", "."},
        {".", "O", "O", ".", ".", "."},
        {".", ".", ".", ".", ".", "."}
    };
    printsRotated(grid);
    }
    public static void printsRotated(String[][] multiArray) {
        //Loops as many times as long is any list inside of the main one.
        for (int i=0; i<multiArray[0].length; i++) {
            //Loops as many times as long is the main list.
            for (int n=0; n<multiArray.length; n++) {
                System.out.print(multiArray[n][i]);
            }
            System.out.println();
        }
    }
}