public class AudioPlayer implements MediaPlayer {

    MediaAdapter ma;

    @Override
    public void play(String audio,String file){
        if(audio.equalsIgnoreCase("mp3")){
            System.out.println("playing in Audioplayer "+file);
        }
        else if(audio.equalsIgnoreCase("vlc")){
            ma = new MediaAdapter(audio);
            ma.play(audio, file);
        }
        else if(audio.equalsIgnoreCase("mp4")){
            ma = new MediaAdapter(audio);
            ma.play(audio, file);
        }
        else{
            System.out.println("invalid");
        }
    }
    
}
