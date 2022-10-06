
class User extends Account{
    String address;
    public User(String name, String document,String address) {
        super(name, document);
        this.address = address;
    }

}
