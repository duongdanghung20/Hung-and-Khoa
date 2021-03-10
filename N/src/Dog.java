public class Dog extends Animal{
    private int size;
    private String breed;
    public void Dog(int size, String breed)
    {
        this.size = size;
        this.breed = breed;
    }
    public void bark(int numberOfBarks)
    {
        if (numberOfBarks>0)
        {
            for (int i = 0; i<numberOfBarks;i++)
            {
                System.out.println("Gau!");
            }
        }
    }
    public void makeNoise()
    {
        System.out.println("Grrrrrrrrr...");
    }


    public int getSize() {
        return size;
    }

    public String getBreed() {
        return breed;
    }
}
