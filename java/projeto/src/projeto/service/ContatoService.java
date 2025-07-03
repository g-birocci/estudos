package projeto.service;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import projeto.model.Contato;
import projeto.database.ConexaoBD;

public class ContatoService {
    
    public List<Contato> listarTodos() {
        List<Contato> contatos = new ArrayList<>();
        String sql = "SELECT * FROM contatos";
        
        try {
            Connection conn = ConexaoBD.conectar();
            if (conn != null) {
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql);
                
                while (rs.next()) {
                    Contato contato = new Contato();
                    contato.setId(rs.getLong("id"));
                    contato.setNome(rs.getString("nome"));
                    contato.setTelefone(rs.getString("telefone"));
                    contato.setEmail(rs.getString("email"));
                    contatos.add(contato);
                }
                rs.close();
                stmt.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        
        return contatos;
    }
    
    public List<Contato> buscar(String termo) {
        List<Contato> contatos = new ArrayList<>();
        String sql = "SELECT * FROM contatos WHERE nome LIKE ? OR telefone LIKE ? OR email LIKE ?";
        String termoBusca = "%" + termo + "%";
        
        try {
            Connection conn = ConexaoBD.conectar();
            if (conn != null) {
                PreparedStatement pstmt = conn.prepareStatement(sql);
                pstmt.setString(1, termoBusca);
                pstmt.setString(2, termoBusca);
                pstmt.setString(3, termoBusca);
                
                ResultSet rs = pstmt.executeQuery();
                
                while (rs.next()) {
                    Contato contato = new Contato();
                    contato.setId(rs.getLong("id"));
                    contato.setNome(rs.getString("nome"));
                    contato.setTelefone(rs.getString("telefone"));
                    contato.setEmail(rs.getString("email"));
                    contatos.add(contato);
                }
                rs.close();
                pstmt.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        
        return contatos;
    }
    
    public Contato buscarPorId(Long id) {
        String sql = "SELECT * FROM contatos WHERE id = ?";
        
        try {
            Connection conn = ConexaoBD.conectar();
            if (conn != null) {
                PreparedStatement pstmt = conn.prepareStatement(sql);
                pstmt.setLong(1, id);
                ResultSet rs = pstmt.executeQuery();
                
                if (rs.next()) {
                    Contato contato = new Contato();
                    contato.setId(rs.getLong("id"));
                    contato.setNome(rs.getString("nome"));
                    contato.setTelefone(rs.getString("telefone"));
                    contato.setEmail(rs.getString("email"));
                    rs.close();
                    pstmt.close();
                    return contato;
                }
                rs.close();
                pstmt.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        
        return null;
    }
    
    public void salvar(Contato contato) {
        String sql = "INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)";
        
        try {
            Connection conn = ConexaoBD.conectar();
            if (conn != null) {
                PreparedStatement pstmt = conn.prepareStatement(sql);
                pstmt.setString(1, contato.getNome());
                pstmt.setString(2, contato.getTelefone());
                pstmt.setString(3, contato.getEmail());
                pstmt.executeUpdate();
                pstmt.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    public void atualizar(Contato contato) {
        String sql = "UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?";
        
        try {
            Connection conn = ConexaoBD.conectar();
            if (conn != null) {
                PreparedStatement pstmt = conn.prepareStatement(sql);
                pstmt.setString(1, contato.getNome());
                pstmt.setString(2, contato.getTelefone());
                pstmt.setString(3, contato.getEmail());
                pstmt.setLong(4, contato.getId());
                pstmt.executeUpdate();
                pstmt.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    public void excluir(Long id) {
        String sql = "DELETE FROM contatos WHERE id = ?";
        
        try {
            Connection conn = ConexaoBD.conectar();
            if (conn != null) {
                PreparedStatement pstmt = conn.prepareStatement(sql);
                pstmt.setLong(1, id);
                pstmt.executeUpdate();
                pstmt.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
} 