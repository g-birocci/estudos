package projeto.service;

public class LoginService {
    private static final String USUARIO_CORRETO = "root";
    private static final String SENHA_CORRETA = "123456";
    
    public boolean validarLogin(String usuario, String senha) {
        return USUARIO_CORRETO.equals(usuario) && SENHA_CORRETA.equals(senha);
    }
} 