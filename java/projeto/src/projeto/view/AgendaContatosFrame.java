package projeto.view;

import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;
import java.util.List;
import projeto.service.ContatoService;
import projeto.model.Contato;

public class AgendaContatosFrame extends javax.swing.JFrame {
    private ContatoService contatoService;
    private DefaultTableModel tableModel;

    public AgendaContatosFrame() {
        initComponents();
        contatoService = new ContatoService();
        configurarTabela();
        carregarContatos();
        configurarCampoTelefone();
    }

    private void configurarCampoTelefone() {
        // Adiciona um KeyListener para permitir apenas números
        txtTelefone.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                char c = evt.getKeyChar();
                if (!Character.isDigit(c) && c != java.awt.event.KeyEvent.VK_BACK_SPACE) {
                    evt.consume();
                }
            }
        });
    }

    @SuppressWarnings("unchecked")
    private void initComponents() {
        jPanel1 = new javax.swing.JPanel();
        lblNome = new javax.swing.JLabel();
        lblTelefone = new javax.swing.JLabel();
        lblEmail = new javax.swing.JLabel();
        txtNome = new javax.swing.JTextField();
        txtTelefone = new javax.swing.JTextField();
        txtEmail = new javax.swing.JTextField();
        btnLimpar = new javax.swing.JButton();
        btnAdicionar = new javax.swing.JButton();
        lblBuscar = new javax.swing.JLabel();
        txtBuscar = new javax.swing.JTextField();
        btnBuscar = new javax.swing.JButton();
        btnEditar = new javax.swing.JButton();
        btnExcluir = new javax.swing.JButton();
        lblContatos = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        tblContatos = new javax.swing.JTable();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Agenda de Contatos");

        // Labels
        lblNome.setText("Nome:");
        lblTelefone.setText("Telefone:");
        lblEmail.setText("Email:");
        lblBuscar.setText("Buscar:");
        lblContatos.setText("Contatos:");

        // Buttons
        btnLimpar.setText("Limpar");
        btnLimpar.addActionListener(evt -> limparCampos());

        btnAdicionar.setText("Adicionar");
        btnAdicionar.addActionListener(evt -> adicionarContato());

        btnBuscar.setText("Buscar");
        btnBuscar.addActionListener(evt -> buscarContatos());

        btnEditar.setText("Editar");
        btnEditar.addActionListener(evt -> editarContato());

        btnExcluir.setText("Excluir");
        btnExcluir.addActionListener(evt -> excluirContato());

        // Table
        tblContatos.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {},
            new String [] {"ID", "Nome", "Telefone", "Email"}
        ));
        tblContatos.getSelectionModel().addListSelectionListener(e -> {
            if (!e.getValueIsAdjusting()) {
                int selectedRow = tblContatos.getSelectedRow();
                if (selectedRow >= 0) {
                    txtNome.setText((String) tableModel.getValueAt(selectedRow, 1));
                    txtTelefone.setText((String) tableModel.getValueAt(selectedRow, 2));
                    txtEmail.setText((String) tableModel.getValueAt(selectedRow, 3));
                }
            }
        });
        jScrollPane1.setViewportView(tblContatos);

        // Layout
        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lblNome)
                            .addComponent(lblTelefone)
                            .addComponent(lblEmail))
                        .addGap(10, 10, 10)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(txtNome)
                            .addComponent(txtTelefone)
                            .addComponent(txtEmail)))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGap(0, 0, Short.MAX_VALUE)
                        .addComponent(btnLimpar)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(btnAdicionar))
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(lblBuscar)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(txtBuscar)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(btnBuscar)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(btnEditar)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(btnExcluir))
                    .addComponent(lblContatos)
                    .addComponent(jScrollPane1))
                .addContainerGap())
        );
        
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblNome)
                    .addComponent(txtNome, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblTelefone)
                    .addComponent(txtTelefone, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblEmail)
                    .addComponent(txtEmail, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnLimpar)
                    .addComponent(btnAdicionar))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblBuscar)
                    .addComponent(txtBuscar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnBuscar)
                    .addComponent(btnEditar)
                    .addComponent(btnExcluir))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(lblContatos)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 200, Short.MAX_VALUE)
                .addContainerGap())
        );

        pack();
        setLocationRelativeTo(null);
    }

    private void configurarTabela() {
        String[] colunas = {"ID", "Nome", "Telefone", "Email"};
        tableModel = new DefaultTableModel(colunas, 0) {
            @Override
            public boolean isCellEditable(int row, int column) {
                return false;
            }
        };
        tblContatos.setModel(tableModel);
    }

    private void carregarContatos() {
        tableModel.setRowCount(0);
        List<Contato> contatos = contatoService.listarTodos();
        for (Contato contato : contatos) {
            Object[] row = {
                contato.getId(),
                contato.getNome(),
                contato.getTelefone(),
                contato.getEmail()
            };
            tableModel.addRow(row);
        }
    }

    private void limparCampos() {
        txtNome.setText("");
        txtTelefone.setText("");
        txtEmail.setText("");
        txtBuscar.setText("");
        tblContatos.clearSelection();
    }

    private boolean validarCampos() {
        if (txtNome.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "O campo Nome é obrigatório");
            return false;
        }

        String telefone = txtTelefone.getText().trim();
        if (!telefone.isEmpty()) {
            // Verifica se o telefone contém apenas números
            if (!telefone.matches("\\d+")) {
                JOptionPane.showMessageDialog(this, "O telefone deve conter apenas números");
                return false;
            }
        }

        return true;
    }

    private void adicionarContato() {
        if (validarCampos()) {
            Contato contato = new Contato(
                txtNome.getText(),
                txtTelefone.getText(),
                txtEmail.getText()
            );
            contatoService.salvar(contato);
            limparCampos();
            carregarContatos();
            JOptionPane.showMessageDialog(this, "Contato adicionado com sucesso!");
        }
    }

    private void editarContato() {
        int selectedRow = tblContatos.getSelectedRow();
        if (selectedRow >= 0) {
            if (validarCampos()) {
                Long id = (Long) tableModel.getValueAt(selectedRow, 0);
                Contato contato = new Contato(
                    txtNome.getText(),
                    txtTelefone.getText(),
                    txtEmail.getText()
                );
                contato.setId(id);
                contatoService.atualizar(contato);
                limparCampos();
                carregarContatos();
                JOptionPane.showMessageDialog(this, "Contato atualizado com sucesso!");
            }
        } else {
            JOptionPane.showMessageDialog(this, "Selecione um contato para editar");
        }
    }

    private void excluirContato() {
        int selectedRow = tblContatos.getSelectedRow();
        if (selectedRow >= 0) {
            Long id = (Long) tableModel.getValueAt(selectedRow, 0);
            int confirm = JOptionPane.showConfirmDialog(
                this,
                "Tem certeza que deseja excluir este contato?",
                "Confirmar Exclusão",
                JOptionPane.YES_NO_OPTION
            );
            if (confirm == JOptionPane.YES_OPTION) {
                contatoService.excluir(id);
                limparCampos();
                carregarContatos();
                JOptionPane.showMessageDialog(this, "Contato excluído com sucesso!");
            }
        } else {
            JOptionPane.showMessageDialog(this, "Selecione um contato para excluir");
        }
    }

    private void buscarContatos() {
        String termo = txtBuscar.getText().trim();
        if (!termo.isEmpty()) {
            tableModel.setRowCount(0);
            List<Contato> contatos = contatoService.buscar(termo);
            for (Contato contato : contatos) {
                Object[] row = {
                    contato.getId(),
                    contato.getNome(),
                    contato.getTelefone(),
                    contato.getEmail()
                };
                tableModel.addRow(row);
            }
        } else {
            carregarContatos();
        }
    }

    public static void main(String args[]) {
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(AgendaContatosFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }

        java.awt.EventQueue.invokeLater(() -> {
            new AgendaContatosFrame().setVisible(true);
        });
    }

    // Variables declaration
    private javax.swing.JButton btnAdicionar;
    private javax.swing.JButton btnBuscar;
    private javax.swing.JButton btnEditar;
    private javax.swing.JButton btnExcluir;
    private javax.swing.JButton btnLimpar;
    private javax.swing.JLabel lblNome;
    private javax.swing.JLabel lblTelefone;
    private javax.swing.JLabel lblEmail;
    private javax.swing.JLabel lblBuscar;
    private javax.swing.JLabel lblContatos;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTable tblContatos;
    private javax.swing.JTextField txtNome;
    private javax.swing.JTextField txtTelefone;
    private javax.swing.JTextField txtEmail;
    private javax.swing.JTextField txtBuscar;
} 