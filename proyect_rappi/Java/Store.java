class Store extends Products{
    String name_store;
    public Store(String name, String brand, Integer amount,String name_store){
        super(name, brand, amount);
        this.name_store = name_store;
    }    
}
