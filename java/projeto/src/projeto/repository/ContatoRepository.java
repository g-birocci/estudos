package projeto.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import projeto.model.Contato;

@Repository
public interface ContatoRepository extends JpaRepository<Contato, Long> {
    // Métodos personalizados podem ser adicionados aqui
} 