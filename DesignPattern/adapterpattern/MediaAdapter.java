public class MediaAdapter implements MediaPlayer {

    AdvanceMediaPlayer amp;
    
    public MediaAdapter(String autidtype){

        if(autidtype.equalsIgnoreCase("vlc")){
            amp = new VlcPlayer();
        }
        else if(autidtype.equalsIgnoreCase("mp4")){
            amp = new Mp4();
        }

    }

    @Override
    public void play(String autidtype, String filename) {
        if(autidtype.equalsIgnoreCase("vlc")){
            amp.advanceplay(filename);
        }
        else if(autidtype.equalsIgnoreCase("mp4")){
            amp.advanceplay(filename);
        }
    }

    
}
