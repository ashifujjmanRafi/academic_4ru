
public class demo {

    public static void main(String[] args) {
        
        Student model = new Student();
        model.setName("rafi");
        model.setRoll("10");

        StudentView view = new StudentView();

        Controller control = new Controller(model, view);
        control.updateview();
        
        control.setname("nahid");
        control.setname(model.getName());
        control.updateview();

    }
    
}
