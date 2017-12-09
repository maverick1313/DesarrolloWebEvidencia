package itesm.tweet;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.content.Intent;
import android.os.AsyncTask;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import itesm.usuarios_api.model.MessagesTokenMessage;

import java.util.concurrent.ExecutionException;
import itesm.SyncTaskClass.loginSyncTask;

public class tweet extends AppCompatActivity {

    Button btnLogin;
    EditText edtEmail;
    EditText edtPassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tweet);

        btnLogin = (Button) findViewById(R.id.login);
        edtEmail = (EditText) findViewById(R.id.edtEmail);
        edtPassword = (EditText) findViewById(R.id.edtPassword);

        btnLogin.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {

                String email =  edtEmail.getText().toString().trim();
                String password = edtPassword.getText().toString().trim();

                if ((email.length() == 0) || (password.length() == 0))
                {
                    Toast.makeText(tweet.this,
                            "Necesitas ingresar tu correo y contraseña para iniciar sesión.",
                            Toast.LENGTH_SHORT).show();
                    return;
                }

                String[] params = {email, password};
                Toast.makeText(tweet.this, "Email: " + email + " Password: " + password, Toast.LENGTH_LONG).show();
                AsyncTask<String, Void, MessagesTokenMessage> execute =
                        new loginSyncTask(tweet.this).execute(params);
                String Token = new String();



                /*LoginTask(LoginActivity.this).execute(params);*/
                try {
                    Token = execute.get().getToken();
                    //Toast.makeText(LoginActivity.this,"Token: "+execute.get().getToken(),Toast.LENGTH_SHORT).show();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e){
                    e.printStackTrace();
                }
                finally
                {
                    if(Token != null)
                    {
                        Intent intent = new Intent(tweet.this, MytweetActivity.class);
                        intent.putExtra("Token",Token);
                        startActivity(intent);
                    }

                }
            }
        });
    }




}
