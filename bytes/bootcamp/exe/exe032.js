class Channel {
    constructor(nome) {
        this.nome = nome;
        this.subcribers = []
        this.videos = []
    }

    adicionarSubscriber(subscriber) {
        this.subcribers.push(subscriber);
    }

    adicionarVideo(video) {
        this.videos.push(video)
        this.subcribers.forEach(sub => console.log(sub.notificar(this.nome, video)));

    }

}

class Subscriber {
    constructor(nome) {
        this.nome = nome
    }

    notificar(canalNome, video) {
        return (`${this.nome}, um novo vídeo "${video}" foi adicionado no canal ${canalNome}!`);
    }
}

const canal = new Channel("Canal de Teste");
const usuario = new Subscriber("Gabriel");

canal.adicionarSubscriber(usuario);
canal.adicionarVideo("Como programar em JS");
