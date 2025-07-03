package projeto.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import projeto.model.Contato;
import projeto.service.ContatoService;

@Controller
@RequestMapping("/contatos")
public class ContatoController {

    @Autowired
    private ContatoService contatoService;

    @GetMapping
    public String listarContatos(Model model) {
        model.addAttribute("contatos", contatoService.listarTodos());
        model.addAttribute("novoContato", new Contato());
        return "contatos/lista";
    }

    @GetMapping("/novo")
    public String mostrarFormularioNovo(Model model) {
        model.addAttribute("contato", new Contato());
        return "contatos/formulario";
    }

    @PostMapping("/salvar")
    public String salvarContato(@ModelAttribute Contato contato) {
        contatoService.salvar(contato);
        return "redirect:/contatos";
    }

    @GetMapping("/editar/{id}")
    public String mostrarFormularioEditar(@PathVariable Long id, Model model) {
        Contato contato = contatoService.buscarPorId(id)
                .orElseThrow(() -> new IllegalArgumentException("ID de contato inválido:" + id));
        model.addAttribute("contato", contato);
        return "contatos/formulario";
    }

    @GetMapping("/deletar/{id}")
    public String deletarContato(@PathVariable Long id) {
        contatoService.deletar(id);
        return "redirect:/contatos";
    }
} 