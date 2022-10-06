
class Main {
    public static void main(String[] args){
        System.out.println("bienvenido a rappi los datos añadidos son:");
        Restaurant comida1 = new Restaurant("hot dog","los jochos",2, "junk food", 241022,"los jochos");
        comida1.Print_products();
        Restaurant bebida1 = new Restaurant("red cola", "red cola",2,"refresco",040523,"los jochos");
        bebida1.Print_products();
        
        Drogstore drog_prod = new Drogstore("ketorolako","simialivio", 1, "similares", 310325);
        drog_prod.setAmount(4);
        drog_prod.Print_products();
        drog_prod.print_drog();

        Delivering entrega1 = new Delivering(new User("alicia mendez", "EXPRESS", "..."),new Deliver("javier soza", "DEL"),new Products("jabon", "ACE", 3), new Payment());
        entrega1.setAmount(4);
        entrega1.imp_deliver();
    }   
}
