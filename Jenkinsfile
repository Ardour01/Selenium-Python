pipeline {
    agent any
    parameters{
         choice(name: 'Module Name', choices: "Input_Forms\nProgress_Bars\nTables", description: 'Test module names')
    }

    //options { skipDefaultCheckout() }


    environment {
        EMAIL_RECIPIENT = "example@example.com"

    }

    stages {


        stage('Run the tests') {
            steps {
            sh """
            python3 --version
            pwd
            ls -la
            sudo apt-get install python3-pip python3-setuptools python3.9-venv -y
            ls -la
            pwd

            python3 -m venv .venv
            . .venv/bin/activate
            echo "Activated"
            pip3 install -r requirements.txt
            python3 -m pytest -s tests/test_input_forms.py
            """
            }
        }
    }


    post {
        always {
            echo "Always"
        }

        success {
            echo "SUCCESSFUL"
        }

        failure {
            echo "FAILED"
        }
    }
}