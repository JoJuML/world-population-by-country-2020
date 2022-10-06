class Delivering {
    Integer id;
    User user;
    Products product;
    Deliver deliver;
    Route route;
    Boolean completed;
    Payment payment;

    public Delivering(User user,Deliver deliver,Products product,Payment payment) {
    this.user = user;
    this.deliver = deliver;
    this.product = product;
    this.payment = payment;
    }
    void imp_deliver(){
        System.out.println("la entrega se hace: \n");
        System.out.println("usuario :"+user.name+" con el repartidor: "+deliver.name+ " producto: "+product.name+" brand: "+product.brand);
    }
    public void setAmount(int i) {
    }
}
