interface Kill {
    public void kill();
}
interface Menace{
    public void menace();
}
interface Vampire extends Kill,Menace{
    public void drinkBlood();
}