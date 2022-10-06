class Restaurant extends Products{
    String type_food;
    Integer sell_by_date;
    String name_rest;
    public Restaurant(String name,String brand,Integer amount,String type_food,Integer sell_by_date,String name_rest){
        super(name,brand,amount);
        this.type_food = type_food;
        this.sell_by_date = sell_by_date;
        this.name_rest = name_rest;
    }
}
