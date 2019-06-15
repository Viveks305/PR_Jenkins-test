pipeline {
	agent any 
	stages{
		stage('build'){
			steps {
				bat ''
			}
		}
		
		stage('test') {
			steps{
				bat 'python -m unittest app_test.py'
			}
		}
	
	}
}