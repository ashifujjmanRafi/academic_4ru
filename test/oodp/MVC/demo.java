public class demo{
    public static void main(String[] args) {
        Student  model = new Student();
        View view = new View();

        model.setName("rafi");
        model.setRoll("10");
        // view.printStudentDetails(model.getName(),model.getRoll());
        Controller c1 = new Controller(model, view);
        c1.updateView();
        c1.setStudentName("nahid");
        c1.updateView();
    }
}