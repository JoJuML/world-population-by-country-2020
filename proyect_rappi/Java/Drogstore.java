class Drogstore extends Products{
    String name_drogstore;
    Integer expiration; //expiration date
    public Drogstore(String name, String brand, Integer amount,String name_drogstore,Integer expiration) {
        super(name, brand, amount);
        this.name_drogstore = name_drogstore;
        this.expiration = expiration;
    }
    
    void print_drog(){
    System.out.println("name: " + name +" brand: " + brand + " amount: " + getAmount() + " name of drogstore: " +name_drogstore+" expiration: "+ expiration);
    }
}
