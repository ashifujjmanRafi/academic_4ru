

public class Controller {

    private Student model;
    private StudentView view;

    public Controller(Student model,StudentView view){
        this.model = model;
        this.view = view;

    }
    public void setname(String name){
        model.setName(name);
    }
    public String getname(){
        return model.getName();
    }

    public void setroll(String roll){
        model.setName(roll);
    }
    public String getroll(){
        return model.getRoll();
    }
    
    public void updateview(){
        view.studentDetails(getname(), getroll());
    }
}
