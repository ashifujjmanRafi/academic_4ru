public class Controller {

    private Student model;
    private View view;

    public Controller(Student model,View view){
        this.model = model;
        this.view = view;
    }
    public void setStudentName(String name){
        model.setName(name);
    }
    public String getStudentName(){
        return model.getName();
    }
    public void setStudentRoll(String roll){
        model.setRoll(roll);
    }
    public String getStudentRoll(){
        return model.getRoll();
    }

    public void updateView(){
        view.printStudentDetails(model.getName(),model.getRoll());
    }
    
}
