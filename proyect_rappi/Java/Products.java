

class Products {
    Integer id;
    String name;
    String brand;
    Float cost;
    private Integer amount;
    String type;

    public Products(String name,String brand,Integer amount){
        this.name = name;
        this.brand = brand;
        this.amount = amount;
    }
    
    public Integer getAmount() {
        return amount;
    }

    public void setAmount(Integer amount) {
        if (amount<1){
            System.out.println("debe ser una cantidad mayor a 0");
        }
        else{
            this.amount = amount;
        } 
        
    }

    void Print_products(){
        System.out.println("name: " + name +" brand: " + brand + " amount: " + amount);
    }
}
