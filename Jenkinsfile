pipeline {
	agent any 
	stages{
		stage('build'){
			steps {
				sh 'python -m unittest app_test.py'
			}
		}
		
		stage('test') {
			steps{
				sh ''
			}
		}
	
	}
}
