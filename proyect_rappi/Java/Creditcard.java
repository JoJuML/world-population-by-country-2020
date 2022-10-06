class Creditcard extends Payment{
    int number;
    int date;
    int CVV;
    public Creditcard(int id,int number,int date,int CVV){
        this.number = number;
        this.date = date;
        this.CVV = CVV;
    }
}
