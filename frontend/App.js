import { StatusBar } from 'expo-status-bar';
import { Button,  StyleSheet, Text, View } from 'react-native';
import { Socket, io } from 'socket.io-client';
import { useSpeechRecognition } from 'react-speech-recognition';
import { useRef, useState } from 'react';


//const socket = io.connect("http://192.168.110.39:3000");

export default function App() {
  const [isrec , setrec] = useState(false);
  const { transcript, resetTranscript } = useSpeechRecognition();
  const microphoneRef = useRef(null);

  const startrecording = ()=>{
    setrec(true)
      
        microphoneRef.current.classList.add("listening");
        SpeechRecognition.startListening({
          continuous: true,
        });

  }


  

  const stopRecording = ()=>{
    setrec(false)
    microphoneRef.current.classList.remove("listening");
    SpeechRecognition.stopListening();
  };


    

  
  
  return (
    <View style={styles.container}>
      <Button title='click here' /*onPress={isrec? stopRecording : startrecording} *//>
      {isrec? (<Text>Recording...</Text>):(<></>)}
      <StatusBar style="auto" />
      {/*transcript && (<View>{transcript}</View>)*/}
    </View>
    
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
