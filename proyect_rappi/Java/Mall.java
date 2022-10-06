class Mall extends Products{
    String name_mall;
    public Mall(String name, String brand, Integer amount,String name_mall){
        super(name, brand, amount);
        this.name_mall = name_mall;
    }    
}
