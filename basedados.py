# Exercicio, Aceder a uma DB em  python, ter input do user para fazer acesso(Basedados, user, password:#####)
import sys,psycopg2

def main():
    try:
        conn = psycopg2.connect(
            dbname=sys.argv[0],
            user=sys.argv[1],
            password=sys.argv[2],
            host="localhost",
            port="3306"
        )
        print("✅ Conexão bem-sucedida!")

        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        print("Hora atual no servidor:", result)

        cur.close()
        conn.close()
        print("🔒 Conexão encerrada.")
    except Exception as e:
        print("❌ Erro ao conectar ao banco:", e)

if __name__ == "__main__":
    main()
