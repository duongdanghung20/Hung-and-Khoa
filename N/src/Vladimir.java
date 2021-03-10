public class Vladimir extends veryBadVampire {
    private String name;

    public void setName(String name) {
        this.name = name;
    }
    public void introduce() {
        System.out.print(name);
        kill();
        System.out.print(name);
        drinkBlood();
        menace();
    }
}
