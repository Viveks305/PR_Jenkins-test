pipeline {
	agent any 
	stages{
		stage('build'){
			steps {
				sh ''
			}
		}
		
		stage('test') {
			steps{
				sh 'python -m unittest app_test.py'
			}
		}
	
	}
}
