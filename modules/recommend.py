def get_recommendation(emotion):
    data = {
        "happy": {
            "songs": ["https://youtu.be/_6i4jndlkO0?si=SZ_wTOWHyeI7je_i"],
            "videos": ["https://youtu.be/5dNEFkqQ5Fg?si=brSPooltE9c6TjbI"],
            "podcasts": ["https://open.spotify.com/playlist/38he99wNRz1QU6mrOAeyw9?si=HpmtXuqPTS252r2r-YUX4A"],
            "story": "Happiness grows when shared.",
            "advice": "Keep smiling and enjoy your day!"
        },
        "sad": {
            "songs": ["https://youtu.be/nCNqPgXDYhY?si=4hKzcuNq4-0UJP6t"],
            "videos": ["https://youtu.be/vjIxOy_2cek?si=csBt4u6OOSIrEceH"],
            "podcasts": ["https://open.spotify.com/episode/0YibwFlA2EYOUs1tm9BNtx?si=M0Ug6kWWQuSsgW50RxVLFg"],
            "story": "Every storm passes with time.",
            "advice": "Stay strong. Better days are coming."
        },
        "angry": {
            "songs": ["https://youtu.be/ckdoR1rR5JU?si=OvtU0W_JIe5a0Eqi"],
            "videos": ["https://youtu.be/FPWXVcfvmm4?si=qBaM5atzQTE0Uq0S"],
            "podcasts": ["https://open.spotify.com/episode/6ft9K4PiZEYHbCNFC0jB9h?si=-rq0KwLBRxOX0jJZzdZSPg"],
            "story": "Calm mind brings better decisions.",
            "advice": "Take a deep breath and relax."
        },
        "neutral": {
            "songs": ["https://youtu.be/OMygIYvrGUw?si=PyL9sLnmCAAoLQ9x"],
            "videos": ["https://youtube.com/shorts/-vrZZUYqTl0?si=r9-RHhKksQNPLfKN"],
            "podcasts": ["https://open.spotify.com/playlist/38he99wNRz1QU6mrOAeyw9?si=HpmtXuqPTS252r2r-YUX4A"],
            "story": "Every moment is a fresh start.",
            "advice": "Try something new today!"
        }
    }

    return data.get(emotion, data["neutral"])