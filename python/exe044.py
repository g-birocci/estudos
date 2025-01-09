def vereficar_usuario(usuario_ativo, tem_permissao, tentaivas_restantes):
    return usuario_ativo and tem_permissao and tentaivas_restantes > 0

print(vereficar_usuario(True, True, 1))  # True (tem acesso)
print(vereficar_usuario(True, False, 1))  # False (sem permissão)
print(vereficar_usuario(False, True, 1))  # False (não está ativo)
print(vereficar_usuario(True, True, 0))  # False (sem tentativas restantes)