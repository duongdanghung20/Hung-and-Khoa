public class Animal {
    private String name;
    public void makeNoise()
    {
        System.out.print("Chit chit");
    }
    public void giveVaccine()
    {
        makeNoise();
    }
    public void introduce()
    {
        makeNoise();
        System.out.println(" I'm "+ name);
    }

    public void setName(String name) {
        this.name = name;
    }
}
